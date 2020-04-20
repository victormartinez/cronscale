clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

black:
	black --target-version py37 k8s_cronscale
