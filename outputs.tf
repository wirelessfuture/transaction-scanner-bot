output "id" {
  description = "The ARN of the Lightsail instance."
  value       = aws_lightsail_instance.bf_lightsail.id
}

output "created_at" {
  description = "The timestamp when the instance was created."
  value       = aws_lightsail_instance.bf_lightsail.created_at
}

output "ipv6_addresses" {
  description = "List of IPv6 addresses for the Lightsail instance"
  value       = aws_lightsail_instance.bf_lightsail.ipv6_addresses
}