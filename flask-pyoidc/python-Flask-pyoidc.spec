Name:           python-flask-pyoidc
Version:        3.11.0
Release:        1%{?dist}
Summary:        Flask extension for OpenID Connect authentication.
License:        Apache 2.0
URL:            https://github.com/zamzterz/flask-pyoidc
Source:         https://github.com/zamzterz/Flask-pyoidc/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Flask extension for OpenID Connect authentication.}


%description %_description

%package -n     python3-flask-pyoidc
Summary:        %{summary}

%description -n python3-flask-pyoidc %_description


%prep
%autosetup -p1 -n Flask-pyoidc-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'flask_pyoidc' +auto


%check
%pyproject_check_import -t


%files -n python3-flask-pyoidc -f %{pyproject_files}


%changelog
* Mon Jan 16 2023 lcrpkking <pkwarcraft@gmail.com> - 3.11.0-1
- Initial package
