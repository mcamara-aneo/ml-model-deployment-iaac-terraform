variable "sm-iam-role" {
    type = string
    default = "arn:aws:iam::335059175490:role/aws-sagemaker-for-deploy-ml-model"
    description = "The IAM Role for SageMaker Endpoint Deployment"
}

variable "container-image" {
    type = string
    default = "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3"
    description = "The container you are utilizing for your SageMaker Model"
}

variable "model-data" {
    type = string
    default = "s3://sagemaker-us-east-1-335059175490/model.tar.gz"
    description = "The pre-trained model data/artifacts, replace this with your training job."
}

variable "instance-type" {
    type = string
    default = "ml.t2.medium"
    description = "The instance behind the SageMaker Real-Time Endpoint"
}

variable "memory-size" {
    type = number
    default = 4096
    description = "Memory size behind your Serverless Endpoint"
}

variable "concurrency" {
    type = number
    default = 2
    description = "Concurrent requests for Serverless Endpoint"
}
variable "aws_provider_access_key" {
  type = string
}

variable "aws_provider_secret_key" {
  type = string
}

variable "aws_provider_region" {
  type = string
}