import argparse
from jinja2 import Environment, FileSystemLoader

def render_template(template_filename, output_filename, variables):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_filename)
    output_from_parsed_template = template.render(variables)

    with open(output_filename, 'w') as fh:
        fh.write(output_from_parsed_template)

def main():
    # Setup argparse
    parser = argparse.ArgumentParser(description='Render a Jinja2 deployment template for weatherapp.')
    parser.add_argument('--output', required=True, help='Output filename for the rendered template')
    parser.add_argument('--image_tag', required=True, help='Docker image tag')
    parser.add_argument('--aws_access_key', required=True, help='AWS Access Key')
    parser.add_argument('--aws_secret_key', required=True, help='AWS Secret Key')
    parser.add_argument('--environment', required=True, help='Deployment environment')

    args = parser.parse_args()

    template_file = 'deployment.yaml.j2'
    
    variables = {
        "image_tag": args.image_tag,
        "aws_access_key": args.aws_access_key,
        "aws_secret_key": args.aws_secret_key,
        "environment": args.environment
    }

    render_template(template_file, args.output, variables)

if __name__ == "__main__":
    main()
