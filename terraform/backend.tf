terraform {
  backend "s3" {
    bucket  = "rdg-terraform-state"
    key     = "dev/terraform.tfstate"
    region  = "ap-southeast-1"
    encrypt = true
  }
}
