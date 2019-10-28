# TODO:
# - fix docs

%bcond_with	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	flask_sqlalchemy
Summary:	Flask microframework extension which adds support for the SQLAlchemy SQL toolkit/ORM
Summary(pl.UTF-8):	Rozszerzenie Flask dodające wsparcie dla SQLAlchemy
Name:		python-%{module}
Version:	2.2
Release:	3
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/mitsuhiko/flask-sqlalchemy/releases/download/%{version}/Flask-SQLAlchemy-%{version}.tar.gz
# Source0-md5:	a93e6af389afac6666733e369c06c798
URL:		https://github.com/mitsuhiko/flask-sqlalchemy
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-SQLAlchemy
BuildRequires:	python-flask
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-flask
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	python3-sqlalchemy
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}

%description -n python3-%{module} -l pl.UTF-8

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n Flask-SQLAlchemy-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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
%doc README CHANGES
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/Flask_SQLAlchemy-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README CHANGES
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Flask_SQLAlchemy-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
