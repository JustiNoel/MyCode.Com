import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Users, Target, Award, BookOpen } from 'lucide-react';

const About = () => {
  const values = [
    {
      icon: Target,
      title: 'Excellence',
      description: 'We strive for academic and professional excellence in all our endeavors.',
    },
    {
      icon: Users,
      title: 'Community',
      description: 'Building strong connections among engineering students and fostering collaboration.',
    },
    {
      icon: BookOpen,
      title: 'Learning',
      description: 'Promoting continuous learning and knowledge sharing within our community.',
    },
    {
      icon: Award,
      title: 'Innovation',
      description: 'Encouraging creative thinking and innovative solutions to real-world problems.',
    },
  ];

  const objectives = [
    'To create a supportive community for engineering students at Maseno University',
    'To facilitate knowledge sharing and academic collaboration',
    'To organize technical workshops, seminars, and professional development events',
    'To bridge the gap between academic learning and industry requirements',
    'To promote innovation and entrepreneurship among engineering students',
    'To establish mentorship programs connecting students with industry professionals',
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      <main className="flex-1">
        {/* Hero Section */}
        <section className="bg-gradient-to-r from-primary to-primary-glow text-primary-foreground py-16">
          <div className="container mx-auto px-4">
            <div className="max-w-3xl mx-auto text-center">
              <h1 className="text-4xl md:text-5xl font-bold mb-6">
                About ESAMU
              </h1>
              <p className="text-xl opacity-90 mb-8">
                Engineering Students Association of Maseno University - Building the future through innovation, collaboration, and excellence.
              </p>
              <Badge variant="secondary" className="text-lg px-6 py-2">
                Established 2020
              </Badge>
            </div>
          </div>
        </section>

        {/* Mission & Vision */}
        <section className="py-16 bg-background">
          <div className="container mx-auto px-4">
            <div className="grid md:grid-cols-2 gap-8 max-w-6xl mx-auto">
              <Card>
                <CardHeader>
                  <CardTitle className="text-2xl">Our Mission</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground leading-relaxed">
                    To empower engineering students at Maseno University by creating a vibrant community 
                    that fosters academic excellence, professional development, and innovation. We aim to 
                    bridge the gap between academic learning and industry practice while promoting 
                    collaboration and lifelong learning.
                  </p>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="text-2xl">Our Vision</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground leading-relaxed">
                    To be the leading engineering student association in Kenya, recognized for producing 
                    innovative, ethical, and globally competitive engineers who contribute meaningfully 
                    to society's technological advancement and sustainable development.
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Values */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold mb-4">Our Core Values</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                These values guide everything we do and shape our community culture.
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              {values.map((value, index) => (
                <Card key={index} className="text-center">
                  <CardHeader>
                    <div className="mx-auto w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
                      <value.icon className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{value.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground text-sm">
                      {value.description}
                    </p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Objectives */}
        <section className="py-16 bg-background">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto">
              <div className="text-center mb-12">
                <h2 className="text-3xl font-bold mb-4">Our Objectives</h2>
                <p className="text-muted-foreground">
                  The key goals that drive our association forward.
                </p>
              </div>

              <div className="grid md:grid-cols-2 gap-6">
                {objectives.map((objective, index) => (
                  <Card key={index} className="border-l-4 border-l-primary">
                    <CardContent className="p-6">
                      <p className="text-foreground">{objective}</p>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* History */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto">
              <Card>
                <CardHeader>
                  <CardTitle className="text-2xl">Our History</CardTitle>
                  <CardDescription>
                    The journey of ESAMU from inception to today
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                  <div className="border-l-2 border-primary pl-6 space-y-4">
                    <div>
                      <h3 className="font-semibold text-lg">2020 - Foundation</h3>
                      <p className="text-muted-foreground">
                        ESAMU was founded by a group of passionate engineering students who recognized 
                        the need for a strong student association to foster collaboration and growth.
                      </p>
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg">2021 - First Major Event</h3>
                      <p className="text-muted-foreground">
                        Organized our first major technical symposium, bringing together students, 
                        faculty, and industry professionals.
                      </p>
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg">2022 - Partnership Expansion</h3>
                      <p className="text-muted-foreground">
                        Established partnerships with leading engineering firms and technology companies 
                        in Kenya to provide internship and mentorship opportunities.
                      </p>
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg">2023 - Digital Transformation</h3>
                      <p className="text-muted-foreground">
                        Launched our digital platform to better connect members and streamline communication.
                      </p>
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg">2024 - Present</h3>
                      <p className="text-muted-foreground">
                        Continuing to grow and innovate, with over 500 active members and expanding programs.
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>
      </main>
      
      <Footer />
    </div>
  );
};

export default About;