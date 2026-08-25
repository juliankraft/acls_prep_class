.PHONY: slides clean

slides:
	for f in marp/*.md; do \
		base=$$(basename "$$f" .md); \
		marp "$$f" --output "docs/slides/$$base.html" --allow-local-files --html --theme marp/themes/zhaw.css; \
	done
	rm -rf docs/slides/img && cp -r marp/img docs/slides/img

clean:
	rm -f docs/slides/*.html
	rm -rf docs/slides/img
