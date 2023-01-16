Name:           python-importlib-resources
Version:        5.10.2
Release:        1%{?dist}
Summary:        Read resources from Python packages

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/python/importlib_resources
Source:         %{pypi_source importlib_resources}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'importlib-resources' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-importlib-resources
Summary:        %{summary}

%description -n python3-importlib-resources %_description


%prep
%autosetup -p1 -n importlib_resources-%{version}


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


%files -n python3-importlib-resources -f %{pyproject_files}


%changelog
* Mon Jan 16 2023 lcrpkking <pkwarcraft@gmail.com> - 5.10.2-1
- Initial package