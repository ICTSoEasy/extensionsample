import setuptools

setuptools.setup(
    name="extensionsample",
    packages=['extensionsample'],
    include_package_data=True,
    install_requires=[
        'notebook', 'jupyter_nbextensions_configurator'
    ],
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/extensionsample", [
            "extensionsample/static/index.js", "extensionsample/static/extensionsample.yaml"
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/extensionsample.json"
        ])
    ],
    zip_safe=False
)