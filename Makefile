.POSIX:

.DEFAULT_GOAL := help

# self-documenting function is made based on https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Shows this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg.info/

.PHONY: dist ## create distribution package
dist: 
	@python setup.py sdist bdist_wheel
