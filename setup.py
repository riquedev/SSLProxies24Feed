from setuptools import setup, find_packages

package_name = "SSLProxies24"
package_version = "1.0"

setup(
    name=package_name,
    version=package_version,
    author="Henrique da Silva Santos (rique_dev)",
    author_email="rique_dev@hotmail.com",
    url="https://github.com/riquedev/SSLProxies24Feed",
    install_requires=["requests", "defusedxm"]
)