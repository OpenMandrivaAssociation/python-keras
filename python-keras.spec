Summary:	A deep learning API written in Python
Name:		python-keras
Version:	2.11.0
Release:	1
Source0:	https://github.com/keras-team/keras/archive/refs/tags/v%{version}/keras-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/m/keras/keras-%{version}.tar.gz
License:	Expat
Group:		Development/Python
Url:		https://keras.io/
BuildRequires:	links
#BuildRequires:	markdown
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(h5py)
BuildRequires:	python3dist(keras-applications)
BuildRequires:	python3dist(keras-preprocessing)
BuildRequires:	python3dist(installer)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(numpy)
#BuildRequires:	python3dist(pandas)
BuildRequires:	python3dist(pillow)
BuildRequires:	python3dist(pip)
#BuildRequires:	python3dist(pydot)
BuildRequires:	python3dist(python-distutils-extra)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(theano)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
Keras is a deep learning API written in Python, running on top of the
machine learning platform TensorFlow. It was developed with a focus on
enabling fast experimentation. Being able to go from idea to result as
fast as possible is key to doing good research.

Keras is:
  - Simple   -- but not simplistic. Keras reduces developer cognitive
                load to free you to focus on the parts of the problem
                that really matter.
  - Flexible -- Keras adopts the principle of progressive disclosure
                of complexity: simple workflows should be quick and
                easy, while arbitrarily advanced workflows should be
                possible via a clear path that builds upon what you've
                already learned.
  - Powerful -- Keras provides industry-strength performance and
                scalability: it is used by organizations and companies
                including NASA, YouTube, or Waymo.

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{py3_puresitedir}/docs
%{py3_puresitedir}/keras
%{py3_puresitedir}/*.*-info/

#-----------------------------------------------------------------------

%prep
%autosetup -n keras-%{version}

%build
#&%py_build
python -m installer --destdir="%{buildroot}" *.whl

%install
%py_install

