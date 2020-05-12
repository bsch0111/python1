# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['20200302siftknn.py'],
             pathex=['C:\\Users\\morgan\\DEEPLEARNING\\PythonApplication1\\PythonApplication1\\v0.02\\0.03'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy.core.multiarray'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='20200302siftknn',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
