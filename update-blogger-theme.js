const { google } = require('googleapis');
const fs = require('fs');

const CLIENT_ID = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const BLOG_ID = process.env.BLOG_ID;
const THEME_FILE = process.env.THEME_FILE;

async function updateBloggerTheme() {
  const oauth2Client = new google.auth.OAuth2(CLIENT_ID, CLIENT_SECRET);

  // Configura las credenciales desde un archivo JSON (como se mencionó antes)

  // Configura la API de Blogger
  const blogger = google.blogger('v3');

  try {
    const themeContent = fs.readFileSync(THEME_FILE, 'utf8');

    // Actualiza el tema HTML del blog en Blogger
    const response = await blogger.blogs.update({
      auth: oauth2Client,
      blogId: BLOG_ID,
      requestBody: {
        customTemplate: themeContent,
      },
    });

    console.log('Tema actualizado en Blogger:', response.data);
  } catch (error) {
    console.error('Error al actualizar el tema en Blogger:', error.message);
  }
}

updateBloggerTheme();
