Name:           python-flask-pyoidc
Version:        3.11.0
Release:        1%{?dist}
Summary:        Flask extension for OpenID Connect authentication.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache 2.0
URL:            https://github.com/zamzterz/flask-pyoidc
Source:         https://github.com/zamzterz/Flask-pyoidc/archive/refs/tags/v3.11.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-pyoidc' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-flask-pyoidc
Summary:        %{summary}

%description -n python3-flask-pyoidc %_description


%prep
%autosetup -p1 -n flask-pyoidc-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import -t


%files -n python3-flask-pyoidc -f %{pyproject_files}


%changelog
* Mon Jan 16 2023 lcrpkking <pkwarcraft@gmail.com> - 3.11.0-1
- Initial package
