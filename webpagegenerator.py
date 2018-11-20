#!/usr/bin/env python

# Below script in development

def main():
        for c in alphabet:
        # Read the template of the page
            template = "webpagetemplate.html"
            with open(template) as f:
                alphabettemplate = f.read()
        # Read the body of the page
            body = "bodies/{}body.html".format(c)
            with open(body) as f:
                body = f.read()
        # Write the complete page
            filename = "generatedwebpages/{}.html".format(c)
            page = webpagetemplate.format(filename=filename, body=body)
            with open(filename, "w") as f:
                f.write(page)

if __name__ == '__main__':
    main()
