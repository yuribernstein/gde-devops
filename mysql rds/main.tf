provider "aws" {
  region = "us-east-2"
}

# Create a security group to allow MySQL access
resource "aws_security_group" "mysql_sg" {
  name_prefix = "mysql-sg"

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Open to the world
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a MySQL RDS instance
resource "aws_db_instance" "mysql" {
  identifier              = "weatherapp-db"
  engine                  = "mysql"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20
  db_name                 = "weatherapp"
  username                = "weatherapp"
  password                = "Passw0rd"
  parameter_group_name    = "default.mysql8.0"
  publicly_accessible     = true
  skip_final_snapshot     = true
  vpc_security_group_ids  = [aws_security_group.mysql_sg.id]

  # Optional: Customize backup and maintenance settings
  backup_retention_period = 7
  backup_window           = "07:00-09:00"
  maintenance_window      = "Mon:03:00-Mon:04:00"
}

# Output the RDS endpoint
output "rds_endpoint" {
  value = aws_db_instance.mysql.endpoint
}
