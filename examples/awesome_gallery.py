from panel_gallery import GalleryTemplate, Application
from pathlib import Path

APPLICATIONS_YAML = Path(__file__).parent/"awesome_gallery.yaml"

applications = Application.read(APPLICATIONS_YAML)
GalleryTemplate(
    site="Awesome Panel",
    site_url="./",
    title="Community Gallery",
    description="Awesome Panel resources by the community",
    applications=applications,
).servable()
