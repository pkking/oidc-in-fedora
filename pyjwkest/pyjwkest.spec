Name:           python-pyjwkest
Version:        1.4.2
Release:        1%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://pypi.org/project/pyjwkest/
Source:         %{pypi_source pyjwkest}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyjwkest' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pyjwkest
Summary:        %{summary}

%description -n python3-pyjwkest %_description


%prep
%autosetup -p1 -n pyjwkest-%{version}


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


%files -n python3-pyjwkest -f %{pyproject_files}


%changelog
* Sun Jan 15 2023 lcrpkking <pkwarcraft@gmail.com> - 1.4.2-1
- Initial package