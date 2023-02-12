import tempfile
import os

from obsidian_maker import *

def test_parse_chapter_and_verse():
    test_line = r'1John 1:1	Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς— '
    assert get_chapter_and_verse(test_line) == '1:1'

def test_parse_text():
    test_line = r'1John 1:1	Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς— '
    assert get_text(test_line) == 'Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς— '

def test_file_name():
    assert get_filename('test/1John.txt') == 'ΙΩΑΝΝΟΥ Α'

def test_created_file():
    tmpdir = tempfile.TemporaryDirectory()
    print(tmpdir.name)
    make_obsidian_file(text='test/1John.txt', directory=tmpdir.name)
    target_filename = 'ΙΩΑΝΝΟΥ Α.md'
    assert target_filename in os.listdir(tmpdir.name)
    with open(os.path.join(tmpdir.name, target_filename)) as f:
        assert len(f.readline()) > 0
        assert ' ^1:1' == f.readline().rstrip()
        assert len(f.readline()) > 0
        assert ' ^1:2' == f.readline().rstrip()
