#!/bin/bash

elb-create-lb MyBalanceLoader --listener "protocol=HTTP,lb-port=80,instance-port=80" --listener "protocol=HTTP,lb-port=8080,instance-port=8080"  --availability-zones us-east-1d

elb-configure-healthcheck MyBalanceLoader --healthy-threshold 10 --interval 30 --target HTTP:8080/upload --timeout 5 --unhealthy-threshold 2

as-create-launch-config MyLaunchConfig --image-id ami-99e2d4f0 --instance-type m1.small --monitoring-enabled

as-create-auto-scaling-group MyAutoScalingGroup --availability-zones us-east-1d --launch-configuration MyLaunchConfig --max-size 5 --min-size 2 --desired-capacity 2 --load-balancers MyBalanceLoader

UpPolicyARN=$(as-put-scaling-policy MyScaleUpPolicy --type ChangeInCapacity --auto-scaling-group MyAutoScalingGroup --adjustment 1) 

DownPolicyARN=$(as-put-scaling-policy MyScaleDownPolicy --type ChangeInCapacity --auto-scaling-group MyAutoScalingGroup --adjustment=-1) 

mon-put-metric-alarm --alarm-name MyCloudWatchScaleUp --metric-name CPUUtilization --namespace AWS/EC2 --period 300 --statistic Average --evaluation-periods 1 --threshold 80 --comparison-operator GreaterThanThreshold --alarm-actions $UpPolicyARN, arn:aws:sns:us-east-1:537029293218:MySNS --dimensions AutoScalingGroupName=MyAutoScalingGroup

mon-put-metric-alarm --alarm-name MyCloudWatchScaleDown --metric-name CPUUtilization --namespace AWS/EC2 --period 300 --statistic Average --evaluation-periods 1 --threshold 20 --comparison-operator LessThanThreshold --alarm-actions $DownPolicyARN, arn:aws:sns:us-east-1:537029293218:MySNS --dimensions AutoScalingGroupName=MyAutoScalingGroup

as-put-notification-configuration --auto-scaling-group MyAutoScalingGroup --notification-types autoscaling:EC2_INSTANCE_LAUNCH autoscaling:EC2_INSTANCE_LAUNCH_ERROR autoscaling:EC2_INSTANCE_TERMINATE autoscaling:EC2_INSTANCE_TERMINATE_ERROR autoscaling:TEST_NOTIFICATION --topic-arn arn:aws:sns:us-east-1:537029293218:MySNS



