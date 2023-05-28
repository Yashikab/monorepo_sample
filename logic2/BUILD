python_sources()

pex_binary(name="app", entry_point="hello.py")

poetry_requirements(
    name="poetry",
)

python_tests(name="tests", sources=["test_*.py"])

docker_image(
    name="docker",
    repository="yashikab/pants_test",
    image_tags = ["v1.0.0"]
)
