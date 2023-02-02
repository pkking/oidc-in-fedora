Name:           python-importlib-resources
Version:        5.10.2
Release:        1%{?dist}
Summary:        Read resources from Python packages
License:        Apache 2.0
URL:            https://github.com/python/importlib_resources
Source:         %{pypi_source importlib_resources}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Read resources from Python packages.}


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
%pyproject_save_files 'importlib_resources' +auto


%check
%pyproject_check_import -t


%files -n python3-importlib-resources -f %{pyproject_files}


%changelog
* Mon Jan 16 2023 lcrpkking <pkwarcraft@gmail.com> - 5.10.2-1
- Initial package
