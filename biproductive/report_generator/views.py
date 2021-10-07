import os
from pathlib import Path

import seaborn as sns
import temppathlib
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404

from home.scripts import correlation


# Create your views here.


def download_file(request, file_path):
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404


def generate_md_report(path_dir: Path, user):
    habit_table, productivity_table, corr = correlation(user)
    print(productivity_table.columns)

    fig = sns.lineplot(data=productivity_table, x='date', y='brain-activity')
    plot_path = str(path_dir / 'plot.png')
    fig.figure.savefig(plot_path)

    with open(path_dir / "output.md", 'w') as file:
        file.write(habit_table.to_markdown() + "\n\n")
        file.write(f"![plot]({plot_path})\n\n")
        file.write(corr.to_markdown() + "\n\n")


@login_required(redirect_field_name='login')
def download_view(request):
    with temppathlib.TemporaryDirectory() as folder:
        generate_md_report(path_dir=folder.path, user=request.user)

        md_path = str(folder.path / 'output.md')
        pdf_path = str(folder.path / 'output.pdf')
        os.system(f'md2pdf {md_path} {pdf_path}')

        return download_file(request, pdf_path)
