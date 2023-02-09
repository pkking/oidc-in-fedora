Name:           python-oic
Version:        1.4.0
Release:        1%{?dist}
Summary:        Python implementation of OAuth2 and OpenID Connect
License:        Apache-2.0
URL:            https://github.com/OpenIDC/pyoidc/
Source:         %{pypi_source oic}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Python implementation of OAuth2 and OpenID Connect.}


%description %_description

%package -n     python3-oic
Summary:        %{summary}

%description -n python3-oic %_description


%prep
%autosetup -p1 -n oic-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'oic' +auto


%check
%pyproject_check_import -t


%files -n python3-oic -f %{pyproject_files}


%changelog
* Sun Jan 15 2023 lcrpkking <pkwarcraft@gmail.com> - 1.4.0-1
- Initial package
