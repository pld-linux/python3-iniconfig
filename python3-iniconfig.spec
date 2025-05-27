#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Brain-dead simple config-ini parsing
Summary(pl.UTF-8):	Bezmyślnie prosta analiza formatu config-ini
Name:		python3-iniconfig
Version:	2.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/iniconfig/
Source0:	https://files.pythonhosted.org/packages/source/i/iniconfig/iniconfig-%{version}.tar.gz
# Source0-md5:	437ede5b20b0ab2e76ca08f02b5c49dd
URL:		https://pypi.org/project/iniconfig/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling >= 1.26
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iniconfig is a small and simple INI-file parser module.

%description -l pl.UTF-8
iniconfig to mały i prosty moduł parsera plików INI.

%prep
%setup -q -n iniconfig-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd)/src \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest testing
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/iniconfig
%{py3_sitescriptdir}/iniconfig-%{version}.dist-info
