# Terraform block
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# Providers
# AWS
provider "aws" {
  profile = "default"
  region  = "eu-central-1"
}

# Resources
# AWS Lightsail instance
resource "aws_lightsail_instance" "ws_lightsail" {
  name              = "wallet_scanner_bot"
  availability_zone = "eu-central-1a"
  blueprint_id      = "ubuntu_20_04"
  bundle_id         = "micro_2_0"
  key_pair_name     = "blockchain-frontier-bot"

  provisioner "file" {
    source      = "launch-script.sh"
    destination = "/tmp/launch-script.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/launch-script.sh",
      "sudo /tmp/launch-script.sh",
    ]
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    password    = ""
    private_key = file(var.keyPath)
    host        = self.ipv6_address
  }
}