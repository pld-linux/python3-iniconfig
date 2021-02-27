#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Brain-dead simple config-ini parsing
Summary(pl.UTF-8):	Bezmyślnie prosta analiza formatu config-ini
Name:		python-iniconfig
Version:	1.1.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/iniconfig/
Source0:	https://files.pythonhosted.org/packages/source/i/iniconfig/iniconfig-%{version}.tar.gz
# Source0-md5:	0b7f3be87481211c183eae095bcea6f1
URL:		https://pypi.org/project/iniconfig/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools >= 41.2.0
BuildRequires:	python-setuptools_scm >= 3
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 41.2.0
BuildRequires:	python3-setuptools_scm >= 3
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iniconfig is a small and simple INI-file parser module.

%description -l pl.UTF-8
iniconfig to mały i prosty moduł parsera plików INI.

%package -n python3-iniconfig
Summary:	Brain-dead simple config-ini parsing
Summary(pl.UTF-8):	Bezmyślnie prosta analiza formatu config-ini
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-iniconfig
iniconfig is a small and simple INI-file parser module.

%description -n python3-iniconfig -l pl.UTF-8
iniconfig to mały i prosty moduł parsera plików INI.

%prep
%setup -q -n iniconfig-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest testing
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest testing
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.txt example.ini
%{py_sitescriptdir}/iniconfig
%{py_sitescriptdir}/iniconfig-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-iniconfig
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.txt example.ini
%{py3_sitescriptdir}/iniconfig
%{py3_sitescriptdir}/iniconfig-%{version}-py*.egg-info
%endif
