import { useQuery } from "@tanstack/react-query";
import { supabase } from "@/integrations/supabase/client";
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Link } from 'react-router-dom';
import { Calendar, Users, Megaphone, BookOpen, ArrowRight, TrendingUp } from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';

const Index = () => {
  const { user } = useAuth();

  // Fetch recent announcements
  const { data: announcements } = useQuery({
    queryKey: ['recent-announcements'],
    queryFn: async () => {
      const { data, error } = await supabase
        .from('announcements')
        .select('*')
        .order('created_at', { ascending: false })
        .limit(3);
      
      if (error) throw error;
      return data;
    },
  });

  // Fetch upcoming events
  const { data: events } = useQuery({
    queryKey: ['upcoming-events'],
    queryFn: async () => {
      const { data, error } = await supabase
        .from('events')
        .select('*')
        .gte('start_date', new Date().toISOString())
        .order('start_date', { ascending: true })
        .limit(3);
      
      if (error) throw error;
      return data;
    },
  });

  const features = [
    {
      icon: Megaphone,
      title: 'Stay Informed',
      description: 'Get the latest announcements and updates from ESAMU leadership and university administration.',
      link: '/announcements'
    },
    {
      icon: Calendar,
      title: 'Upcoming Events',
      description: 'Discover workshops, seminars, competitions, and social events happening in our community.',
      link: '/events'
    },
    {
      icon: Users,
      title: 'Connect & Collaborate',
      description: 'Join discussions, share projects, and collaborate with fellow engineering students.',
      link: '/community'
    },
    {
      icon: BookOpen,
      title: 'Learning Resources',
      description: 'Access study materials, project ideas, and academic resources shared by the community.',
      link: '/resources'
    }
  ];

  const stats = [
    { label: 'Active Members', value: '500+' },
    { label: 'Events Hosted', value: '50+' },
    { label: 'Projects Completed', value: '100+' },
    { label: 'Industry Partners', value: '20+' }
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      <main className="flex-1">
        {/* Hero Section */}
        <section className="relative bg-gradient-to-br from-primary via-primary-glow to-accent text-primary-foreground py-20 overflow-hidden">
          <div className="absolute inset-0 bg-black/10"></div>
          <div className="container mx-auto px-4 relative z-10">
            <div className="max-w-4xl mx-auto text-center">
              <h1 className="text-5xl md:text-6xl font-bold mb-6 leading-tight">
                Welcome to <span className="text-accent">ESAMU</span>
              </h1>
              <p className="text-xl md:text-2xl mb-8 opacity-90 leading-relaxed">
                Engineering Students Association of Maseno University - 
                Your gateway to innovation, collaboration, and professional growth.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                {!user ? (
                  <>
                    <Button size="lg" variant="secondary" asChild>
                      <Link to="/auth">
                        Join Our Community
                        <ArrowRight className="ml-2 h-4 w-4" />
                      </Link>
                    </Button>
                    <Button size="lg" variant="outline" className="border-white text-white hover:bg-white hover:text-primary" asChild>
                      <Link to="/about">Learn More</Link>
                    </Button>
                  </>
                ) : (
                  <>
                    <Button size="lg" variant="secondary" asChild>
                      <Link to="/community">
                        Explore Community
                        <ArrowRight className="ml-2 h-4 w-4" />
                      </Link>
                    </Button>
                    <Button size="lg" variant="outline" className="border-white text-white hover:bg-white hover:text-primary" asChild>
                      <Link to="/events">View Events</Link>
                    </Button>
                  </>
                )}
              </div>
            </div>
          </div>
        </section>

        {/* Stats Section */}
        <section className="py-16 bg-background">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto">
              {stats.map((stat, index) => (
                <div key={index} className="text-center">
                  <div className="text-3xl md:text-4xl font-bold text-primary mb-2">
                    {stat.value}
                  </div>
                  <div className="text-muted-foreground">
                    {stat.label}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">
                What We Offer
              </h2>
              <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
                Discover the tools and resources that make ESAMU the premier platform for engineering students.
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              {features.map((feature, index) => (
                <Card key={index} className="group hover:shadow-lg transition-shadow duration-300">
                  <CardHeader>
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
                      <feature.icon className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{feature.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <CardDescription className="mb-4">
                      {feature.description}
                    </CardDescription>
                    <Button variant="outline" size="sm" asChild>
                      <Link to={feature.link}>
                        Explore
                        <ArrowRight className="ml-2 h-3 w-3" />
                      </Link>
                    </Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Recent Content */}
        <section className="py-16 bg-background">
          <div className="container mx-auto px-4">
            <div className="grid lg:grid-cols-2 gap-12">
              {/* Recent Announcements */}
              <div>
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-2xl font-bold">Latest Announcements</h2>
                  <Button variant="outline" size="sm" asChild>
                    <Link to="/announcements">View All</Link>
                  </Button>
                </div>
                <div className="space-y-4">
                  {announcements?.map((announcement) => (
                    <Card key={announcement.id} className="hover:shadow-md transition-shadow">
                      <CardHeader className="pb-3">
                        <div className="flex items-start justify-between">
                          <Badge variant={announcement.category === 'urgent' ? 'destructive' : 'secondary'}>
                            {announcement.category}
                          </Badge>
                          <span className="text-xs text-muted-foreground">
                            {new Date(announcement.created_at).toLocaleDateString()}
                          </span>
                        </div>
                        <CardTitle className="text-lg line-clamp-2">
                          {announcement.title}
                        </CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-muted-foreground text-sm line-clamp-2 mb-2">
                          {announcement.content}
                        </p>
                        <p className="text-xs text-muted-foreground">
                          By ESAMU Admin
                        </p>
                      </CardContent>
                    </Card>
                  )) || (
                    <Card>
                      <CardContent className="p-6 text-center text-muted-foreground">
                        No announcements yet. Check back soon!
                      </CardContent>
                    </Card>
                  )}
                </div>
              </div>

              {/* Upcoming Events */}
              <div>
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-2xl font-bold">Upcoming Events</h2>
                  <Button variant="outline" size="sm" asChild>
                    <Link to="/events">View All</Link>
                  </Button>
                </div>
                <div className="space-y-4">
                  {events?.map((event) => (
                    <Card key={event.id} className="hover:shadow-md transition-shadow">
                      <CardHeader className="pb-3">
                        <div className="flex items-start justify-between">
                          <Badge variant="outline">
                            {event.category}
                          </Badge>
                          <span className="text-xs text-muted-foreground">
                            {new Date(event.start_date).toLocaleDateString()}
                          </span>
                        </div>
                        <CardTitle className="text-lg line-clamp-2">
                          {event.title}
                        </CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-muted-foreground text-sm line-clamp-2 mb-2">
                          {event.description}
                        </p>
                        {event.location && (
                          <p className="text-xs text-muted-foreground">
                            📍 {event.location}
                          </p>
                        )}
                      </CardContent>
                    </Card>
                  )) || (
                    <Card>
                      <CardContent className="p-6 text-center text-muted-foreground">
                        No upcoming events. Stay tuned for exciting opportunities!
                      </CardContent>
                    </Card>
                  )}
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        {!user && (
          <section className="py-16 bg-primary text-primary-foreground">
            <div className="container mx-auto px-4 text-center">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">
                Ready to Join ESAMU?
              </h2>
              <p className="text-lg mb-8 opacity-90 max-w-2xl mx-auto">
                Become part of a thriving community of engineering students. Connect, learn, and grow with us.
              </p>
              <Button size="lg" variant="secondary" asChild>
                <Link to="/auth">
                  Get Started Today
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Link>
              </Button>
            </div>
          </section>
        )}
      </main>
      
      <Footer />
    </div>
  );
};

export default Index;