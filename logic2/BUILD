python_sources(name="logic2")

pex_binary(name="logic2_app", entry_point="hello.py")

poetry_requirements(
    name="poetry",
)

python_tests(name="logic2_tests", sources=["test_*.py"], dependencies=["logic2"])

docker_image(
    name="docker",
    repository="yashikab/pants_test",
    image_tags = ["v1.0.0"]
)
