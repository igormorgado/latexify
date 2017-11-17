from setuptools import setup

setup(
    name = 'latexify',
    version = '0.0.1',
    #packages = ['latexify'],
    #package_dir = {'latexify': 'src'},
    py_modules = ['latexify'],
    install_requires = [ 'ipython' ],
    description = 'Convert numpy structures to latex display',
    url = 'http://github.com/igormorgado/latexify',
    license = 'GNU/GPLv2',
    python_requires = '>=3.4, <4',
    author = 'Igor Morgado',
    author_email = 'morgado.igor@gmail.com',
    keywords = ['latex', 'numpy', 'jupyter'],
    classifiers = [
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Other Environment",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Education",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    long_description = """\
Convert numpy data structures to a friendly LaTeX
-------------------------------------------------

More description will come."""

)
