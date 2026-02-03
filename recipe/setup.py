from setuptools import setup

setup(
    name='clawpack',
    version='5.14.0',
    packages=[
        'clawpack',
        'clawpack.amrclaw',
        'clawpack.classic',
        'clawpack.clawutil',
        'clawpack.geoclaw',
        'clawpack.pyclaw',
        'clawpack.riemann',
        'clawpack.visclaw',
    ],
    package_dir={
        'clawpack': 'clawpack',
        'clawpack.amrclaw': 'amrclaw/src/python/amrclaw',
        'clawpack.classic': 'classic/src/python/classic',
        'clawpack.clawutil': 'clawutil/src/python/clawutil',
        'clawpack.geoclaw': 'geoclaw/src/python/geoclaw',
        'clawpack.pyclaw': 'pyclaw/src/pyclaw',
        'clawpack.riemann': 'riemann',
        'clawpack.visclaw': 'visclaw/src/python/visclaw',
    },
    install_requires=['numpy', 'matplotlib', 'six'],
    include_package_data=True,
    zip_safe=False,
)
