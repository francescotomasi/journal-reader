import { useEffect, useRef } from 'react';
import { useLocation, useNavigationType } from 'react-router-dom';

const scrollPositions: Record<string, number> = {};

export function useScrollRestoration(loading: boolean = false) {
  const location = useLocation();
  const navigationType = useNavigationType();
  const loadedRef = useRef(false);

  useEffect(() => {
    // Save scroll position when leaving the page or before unmount
    const handleScroll = () => {
      if (!loading) {
        scrollPositions[location.key] = window.scrollY;
      }
    };
    
    // Throttle or just add event listener
    window.addEventListener('scroll', handleScroll, { passive: true });
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [location.key, loading]);

  useEffect(() => {
    // Restore scroll position
    if (!loading && !loadedRef.current) {
      loadedRef.current = true;
      if (navigationType === 'POP' && scrollPositions[location.key] !== undefined) {
        // Wait a tick for React to fully render the DOM
        setTimeout(() => {
          window.scrollTo(0, scrollPositions[location.key]);
        }, 10);
      }
    }
  }, [location.key, navigationType, loading]);
}
