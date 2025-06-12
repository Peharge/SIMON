# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

import os
import sys
import datetime
import chardet
import logging

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon, QPalette, QFont, QPixmap, QImageReader, QSyntaxHighlighter, QTextCharFormat
from PyQt6.QtWidgets import (
    QApplication, QLabel, QScrollArea, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,
    QTextBrowser, QStackedWidget, QSplitter
)

# Optional syntax highlighting
try:
    from pygments import highlight
    from pygments.lexers import get_lexer_for_filename
    from pygments.formatters import HtmlFormatter
    PYGMENTS_AVAILABLE = True
except ImportError:
    PYGMENTS_AVAILABLE = False

# Basic Python highlighter for QTextEdit fallback
class PythonHighlighter(QSyntaxHighlighter):
    keywords = [
        'def', 'class', 'if', 'elif', 'else', 'while', 'for', 'in', 'try', 'except', 'finally',
        'with', 'as', 'return', 'import', 'from', 'pass', 'break', 'continue', 'and', 'or', 'not', 'None', 'True', 'False'
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.formats = {}
        fmt_keyword = QTextCharFormat()
        fmt_keyword.setForeground(QColor('#c586c0'))
        fmt_keyword.setFontWeight(QFont.Weight.Bold)
        for word in self.keywords:
            self.formats[word] = fmt_keyword

    def highlightBlock(self, text):
        for word, fmt in self.formats.items():
            index = text.find(word)
            while index != -1:
                length = len(word)
                self.setFormat(index, length, fmt)
                index = text.find(word, index + length)

class FileDisplayWidget(QStackedWidget):
    """Manages display of text, markdown, and images"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text_view = QTextBrowser()
        self.text_view.setFont(QFont("Courier New", 12))

        self.image_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.image_label.setScaledContents(True)

        self.addWidget(self.text_view)
        self.addWidget(self.image_label)

    def display_image(self, path, container_size):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            raise ValueError(f"Cannot load image: {path}")
        scaled = pixmap.scaled(container_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled)
        self.setCurrentWidget(self.image_label)

    def display_markdown(self, content):
        self.text_view.setMarkdown(content)
        self.setCurrentWidget(self.text_view)

    def display_html(self, html):
        self.text_view.setHtml(html)
        self.setCurrentWidget(self.text_view)

    def display_text(self, content):
        self.text_view.setPlainText(content)
        self.setCurrentWidget(self.text_view)

class FileExplorer(QWidget):
    """A professional file explorer with syntax highlighting and image support."""
    SUPPORTED_IMAGE_EXT = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico'}
    SUPPORTED_MARKDOWN_EXT = {'.md', '.markdown'}
    SUPPORTED_CODE_EXT = {'.py', '.cpp', '.c', '.h', '.bat', '.js', '.java', '.html', '.css'}

    def __init__(self, root_dir=None):
        super().__init__()
        logging.basicConfig(level=logging.INFO)
        self.setWindowTitle("P-Term File Explorer ~/PycharmProjects/SIMON/")
        self.resize(1200, 800)

        self.root_dir = root_dir or os.path.expanduser("~/PycharmProjects/SIMON/")

        self._setup_ui()
        self.apply_styles()
        self.set_dark_mode()
        self.load_directory_structure()

    def _setup_ui(self):
        layout = QVBoxLayout(self)

        # Vertical splitter: file tree above, content viewer below
        splitter = QSplitter(Qt.Orientation.Vertical)

        # File tree
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Type", "Size", "Modified"])
        self.tree.itemClicked.connect(self.on_item_clicked)
        splitter.addWidget(self.tree)

        # Content display area below file tree
        self.content = FileDisplayWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.content)
        splitter.addWidget(self.scroll)

        # Initial splitter sizes
        splitter.setSizes([400, 400])

        layout.addWidget(splitter)

        # Status bar
        self.status = QLabel("Ready")
        layout.addWidget(self.status)

        # Window icon
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))

    def set_dark_mode(self):
        pal = QPalette()
        pal.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        pal.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        self.setPalette(pal)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
                color: #FFFFFF;
                font-family: 'Roboto', sans-serif;
                font-size: 14px;
            }

            QLineEdit {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: 1px solid #778899;
                border-radius: 5px;
                padding: 5px;
                color: #FFFFFF;
            }

            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                color: #FFFFFF;
            }

            QPushButton:hover {
                background-color: #1c2833;
            }

            QTreeWidget {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
            }

            QTreeWidget::item {
                padding: 8px;
                border-bottom: 1px solid #778899;
            }

            QTreeWidget::item:selected {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
                color: #FFFFFF;
            }

            QHeaderView::section {
                background-color: transparent;
                padding: 8px;
                border: none;
            }

            QScrollArea {
                border: none;
                background-color: transparent;
            }

            QScrollBar:vertical {
                background-color: transparent;  /* Hintergrund (Schiene) in transparent */
                width: 10px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff;  /* Schieber (Block) in Weiß */
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: transparent;
            }

            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: transparent;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }

            QScrollBar:horizontal {
                background-color: transparent;  /* Auch der horizontale Balken in transparent */
                height: 10px;
                border-radius: 5px;
            }

            QScrollBar::handle:horizontal {
                background-color: #ffffff;
                min-width: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: transparent;
            }

            QScrollBar::left-arrow:horizontal,
            QScrollBar::right-arrow:horizontal {
                background: transparent;
            }

            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: transparent;
            }

            QLabel {
                background: transparent;
                font-size: 16px;
            }

            QTextEdit {
                background-color: transparent;
                color: #FFFFFF;
                border: 1px solid #778899;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
        """)

    def load_directory_structure(self):
        self.tree.clear()
        self._add_entries(self.root_dir, None)
        self.status.setText(f"Loaded: {self.root_dir}")

    def _add_entries(self, path, parent_item):
        try:
            entries = sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError:
            logging.warning(f"Permission denied: {path}")
            return
        for entry in entries:
            if entry.name.startswith('.'):
                continue
            item = QTreeWidgetItem([
                entry.name,
                'Dir' if entry.is_dir() else 'File',
                self._format_size(entry.stat().st_size) if entry.is_file() else '',
                datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            ])
            item.setData(0, Qt.ItemDataRole.UserRole, entry.path)
            if parent_item:
                parent_item.addChild(item)
            else:
                self.tree.addTopLevelItem(item)
            if entry.is_dir():
                self._add_entries(entry.path, item)

    def _format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}TB"

    def on_item_clicked(self, item):
        path = item.data(0, Qt.ItemDataRole.UserRole)
        if not os.path.isfile(path):
            return
        ext = os.path.splitext(path)[1].lower()
        self.status.setText(f"Opening {os.path.basename(path)}")
        try:
            if ext in self.SUPPORTED_IMAGE_EXT and QImageReader(path).canRead():
                size = self.scroll.viewport().size()
                self.content.display_image(path, size)
            elif ext in self.SUPPORTED_MARKDOWN_EXT:
                with open(path, 'r', encoding='utf-8') as f:
                    self.content.display_markdown(f.read())
            elif ext in self.SUPPORTED_CODE_EXT and PYGMENTS_AVAILABLE:
                code = open(path, 'r', encoding='utf-8', errors='replace').read()
                lexer = get_lexer_for_filename(path, stripall=True)
                html = highlight(code, lexer, HtmlFormatter(full=True, style='monokai'))
                self.content.display_html(html)
            else:
                raw = open(path, 'rb').read()
                enc = chardet.detect(raw)['encoding'] or 'utf-8'
                txt = raw.decode(enc, errors='replace')
                self.content.display_text(txt)
        except Exception as e:
            logging.error(e)
            self.content.display_text(f"Error: {e}")
            self.status.setText("Failed to display content.")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        height = self.height()
        self.tree.setColumnWidth(0, int(self.width() * 0.5))
        for i in range(1, 4):
            self.tree.setColumnWidth(i, int(self.width() * 0.15))
        if self.content.currentWidget() == self.content.image_label:
            pixmap = self.content.image_label.pixmap()
            if pixmap:
                scaled = pixmap.scaled(self.scroll.viewport().size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.content.image_label.setPixmap(scaled)


def main():
    app = QApplication(sys.argv)
    explorer = FileExplorer()
    explorer.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()