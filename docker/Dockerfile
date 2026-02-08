# Use AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.11

# Copy requirements first for better layer caching
COPY lambda-src/requirements.txt ${LAMBDA_TASK_ROOT}/

# Install Python dependencies
RUN pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Copy Lambda function code
COPY lambda-src/index.py ${LAMBDA_TASK_ROOT}/

# Lambda runtime will call this handler
CMD ["index.handler"]
