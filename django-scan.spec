Name: django-scan
Version: 0.1
Release: 1%{?dist}
Summary: django scan test

Group: Application/Internet
License: MIT-like
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-%{version}-venv.tar.gz
BuildArch: noarch

Requires: python
Requires: python-virtualenv
Requires: httpd
Requires: mod_wsgi

%define VENV %{name}-%{version}-venv

%description
a test for make rpm for django project

%prep
echo $RPM_BUILD_ROOT
tar -xf %{SOURCE0}


%build
# inin venv and install requirements
cd %{name}-%{version}
sed -i 's/DEBUG = True/DEBUG = False/g' Learning/settings.py
sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\'\*\'\]/g" Learning/settings.py


%install
cd %{name}-%{version}
virtualenv .venv --setuptools --no-site-packages -q
source ./.venv/bin/activate
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple
tar -zcf %{name}-%{version}-venv.tar.gz ./.venv/

python manage.py collectstatic --no-input
python manage.py compress --force
python manage.py makemigrations && python manage.py migrate
python manage.py makemigrations scan && python manage.py migrate

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__install} -m 0644 django-scan-httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

# create dir
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -d %{buildroot}%{_sysconfdir}/%{name}/

mv * %{buildroot}%{_sysconfdir}/%{name}/
tar -zxf %{buildroot}%{_sysconfdir}/%{name}/%{name}-%{version}-venv.tar.gz
rm %{buildroot}%{_sysconfdir}/%{name}/%{name}-%{version}-venv.tar.gz

%files
%defattr(-, apache, apache)
%{_sysconfdir}/%{name}
%{_sysconfdir}/httpd/conf.d/django-scan-httpd.conf

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD
