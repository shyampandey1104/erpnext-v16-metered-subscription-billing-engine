from setuptools import setup, find_packages

setup(
    name="metered_subscription_billing",
    version="16.0.0",
    description="ERPNext v16 Metered Subscription & Usage-Based Billing - Official Frappe & ERPNext v16 App",
    author="Shyamkumar Pandey",
    author_email="shyampandey1104@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"]
)
