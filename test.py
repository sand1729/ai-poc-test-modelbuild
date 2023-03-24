input_data ="s3://sagemaker-us-east-1-396817003399/iris/iris_data.csv"
print(f'input_data.split("/"): {input_data.split("/")}')
bucket = input_data.split("/")[2]
key = "/".join(input_data.split("/")[3:])
print(f"key: {key}")
print(f"bucket: {bucket}")