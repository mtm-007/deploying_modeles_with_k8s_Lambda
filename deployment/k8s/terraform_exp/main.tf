provider "aws" {
  region = "us-west-2"
  access_key = "aws_access_key"
  secret_key = "aws_secret_key"
}

resource "aws_vpc" "tf-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "tf-trail-vpc-01"
  }
}

resource "aws_subnet" "subnet-01" {
  vpc_id     = aws_vpc.tf-vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "tf-trail-subnet-01"
  }
}

# resource "aws_instance" "terraform-aws-01" {
#   ami           = "ami-04dd23e62ed049936"  
#   instance_type = "t3.micro"
#   tags = {
#     #Name = "ubuntu"
#   }
#}