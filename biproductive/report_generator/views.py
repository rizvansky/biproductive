import os
from datetime import datetime
from pathlib import Path

import seaborn as sns
import temppathlib
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from matplotlib import pyplot as plt

from home.scripts import correlation


# Create your views here.


def download_file(request, file_path):
    try:
        file_name = f'habit-report-{datetime.now().date()}.pdf'
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    except Exception:
        raise Http404


def generate_md_report(path_dir: Path, user):
    habit_table, productivity_table, corr = correlation(user)
    plt.figure(figsize=(6, 3))
    plt.xticks(rotation=20)
    fig = sns.lineplot(data=productivity_table, x='date', y='brain-activity')
    plot_path = str(path_dir / 'plot.png')
    plt.tight_layout()
    fig.figure.savefig(plot_path)

    with open(path_dir / "output.md", 'w') as file:
        file.write(f'# Weekly report, generated in {datetime.now().date()}\n')
        file.write("### Weekly habit statistics\n")
        file.write(habit_table.to_markdown() + "\n")
        file.write("### Weekly brain activity plot\n")
        file.write(f"![plot]({plot_path})\n")
        file.write("### Weekly correlation analysis of habits\n")
        file.write(corr.to_markdown() + "\n")


@login_required(redirect_field_name='login')
def download_view(request):
    with temppathlib.TemporaryDirectory() as folder:
        generate_md_report(path_dir=folder.path, user=request.user)

        md_path = str(folder.path / 'output.md')
        pdf_path = str(folder.path / 'output.pdf')
        os.system(f'md2pdf {md_path} {pdf_path}')

        return download_file(request, pdf_path)
