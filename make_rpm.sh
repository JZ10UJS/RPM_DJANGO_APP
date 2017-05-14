$cwd=`pwd`
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

python setup.py sdist
cp sdist/django-scan-0.1.tar.gz ~/rpmbuild/SOURCES/
cp django-scan.spec ~/rpmbuild/SPECS/

rpmbuild -bb ~/rpmbuild/SPECS/django-scan.spec