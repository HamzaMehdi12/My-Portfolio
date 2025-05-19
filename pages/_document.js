import { Html, Head, Main, NextScript } from 'next/document';

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <meta name="description" content="Personal portfolio site of Hamza Mehdi offering design, engineering, and consulting services." />
        <meta name="keywords" content="Hamza Mehdi, Portfolio, Services, Projects, Design Engineering, Web Development" />
        <meta name="author" content="Hamza Mehdi" />
        <meta property="og:title" content="Hamza Mehdi Portfolio & Services" />
        <meta property="og:description" content="Explore projects, services, and expertise by Hamza Mehdi." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://hamzamehdi.dev" />
        <meta property="og:image" content="/public/og-image.png" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
