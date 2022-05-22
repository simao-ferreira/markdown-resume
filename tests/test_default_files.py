from os.path import exists


def test_resume_markdown_file_exists():
    assert exists(f'./../resume/RESUME.md')


def test_simple_style_exists():
    assert exists(f'./../styles/simple-style.css')
