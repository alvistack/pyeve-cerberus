# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-cerberus
Epoch: 100
Version: 1.3.4
Release: 1%{?dist}
BuildArch: noarch
Summary: Lightweight, extensible data validation library for Python
License: ISC
URL: https://github.com/pyeve/cerberus/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Cerberus is a lightweight and extensible data validation library for
Python. Cerberus provides type checking and other base functionality out
of the box and is designed to be non-blocking and easily extensible,
allowing for custom validation. It has no dependancies and is thoroughly
tested. Python 3 version.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-Cerberus
Summary: Lightweight, extensible data validation library for Python
Requires: python3
Requires: python3-setuptools
Provides: python3-Cerberus = %{epoch}:%{version}-%{release}
Provides: python3-cerberus = %{epoch}:%{version}-%{release}
Provides: python3dist(cerberus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cerberus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cerberus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cerberus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cerberus) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Cerberus
Cerberus is a lightweight and extensible data validation library for
Python. Cerberus provides type checking and other base functionality out
of the box and is designed to be non-blocking and easily extensible,
allowing for custom validation. It has no dependancies and is thoroughly
tested. Python 3 version.

%files -n python%{python3_version_nodots}-Cerberus
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-Cerberus
Summary: Lightweight, extensible data validation library for Python
Requires: python3
Requires: python3-setuptools
Provides: python3-Cerberus = %{epoch}:%{version}-%{release}
Provides: python3-cerberus = %{epoch}:%{version}-%{release}
Provides: python3dist(cerberus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cerberus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cerberus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cerberus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cerberus) = %{epoch}:%{version}-%{release}

%description -n python3-Cerberus
Cerberus is a lightweight and extensible data validation library for
Python. Cerberus provides type checking and other base functionality out
of the box and is designed to be non-blocking and easily extensible,
allowing for custom validation. It has no dependancies and is thoroughly
tested. Python 3 version.

%files -n python3-Cerberus
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-cerberus
Summary: Lightweight, extensible data validation library for Python
Requires: python3
Requires: python3-setuptools
Provides: python3-Cerberus = %{epoch}:%{version}-%{release}
Provides: python3-cerberus = %{epoch}:%{version}-%{release}
Provides: python3dist(cerberus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cerberus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cerberus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cerberus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cerberus) = %{epoch}:%{version}-%{release}

%description -n python3-cerberus
Cerberus is a lightweight and extensible data validation library for
Python. Cerberus provides type checking and other base functionality out
of the box and is designed to be non-blocking and easily extensible,
allowing for custom validation. It has no dependancies and is thoroughly
tested. Python 3 version.

%files -n python3-cerberus
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
