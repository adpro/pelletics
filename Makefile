.POSIX:

.DEFAULT_GOAL := help

# self-documenting function is made based on https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Shows this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## clean distribution packages content
	@echo "🧹 Cleaning distribution content.."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/

.PHONY: dist 
dist: ## create distribution package
	@echo "🎁 Creating distribution package"
	@python setup.py sdist bdist_wheel
	@twine check dist/*

.PHONY: pypitest
pypitest: ## upload package to test pypi
	@echo "🚀 Uploading package to TEST PyPi"
	@twine upload -r pypitest --config-file ~/.pypirc dist/*

.PHONY: pypi
pypi: ## upload package to production pypi
	@echo "🚀 Uploading package to PyPi"
	@twine upload -r pypi --config-file ~/.pypirc dist/*