provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "config_bucket" {
  bucket = "weatherapp-configuration"
  acl    = "private"
}

resource "aws_s3_bucket_object" "default_config" {
  bucket = aws_s3_bucket.config_bucket.id
  key    = "configuration/0.0.0/configuration.json"
  source = "../configuration.json"
  acl    = "private"
}

resource "aws_iam_user" "config_user" {
  name = "config-user"
}

resource "aws_iam_access_key" "config_user_key" {
  user = aws_iam_user.config_user.name
}

resource "aws_iam_user_policy" "config_user_policy" {
  name = "config_user_policy"
  user = aws_iam_user.config_user.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:GetObject"],
        Resource = ["${aws_s3_bucket.config_bucket.arn}/configuration/*"],
        Effect   = "Allow"
      }
    ]
  })
}

output "access_key_id" {
  value = aws_iam_access_key.config_user_key.id
}

output "secret_access_key" {
  value = aws_iam_access_key.config_user_key.secret
  sensitive = true
}

# access the sensitive content via tfstate file
# terraform output -json | jq '.secret_access_key.value'