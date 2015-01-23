import java.util.*;

public class ClosestPair {
	
	private static final double EPSILON = 1e-15;
	
	private static Pair minOfThree(Pair p1, Pair p2, Pair p3) {
		double x = p1.getDistance();
		double y = p2.getDistance();
		double z = p3.getDistance();
		if (x < y && x < z) {
			return p1;
		} else if (y < z && y < x) {
			return p2;
		} else {
			return p3;
		}
	}
	
	private static Pair closestSplitPair(List<Point> Px, List<Point> Py, double delta) {
		int numPoints = Px.size();
		int k = numPoints/2;
		double xBar = Px.get(k - 1).getX();
		
		//Create Sy. Ordered (by y-coord) set of Points that have x-coordinate in range [xBar - delta, xBar + delta]
		List<Point> Sy = new ArrayList<Point>();
		
		for (int i = 0; i < numPoints; i++) {
			double xVal = Py.get(i).getX();
			if (xVal > (xBar - delta) && xVal < (xBar + delta)) {
				Sy.add(Py.get(i));
			}
		}
		
		double best = delta;
		Pair bestPair = new Pair();
		if (Sy.size() < 8){ //if the number of Points in Sy is less than 8, use the bruteForce method
			Pair currentPair = bruteForce(Sy);
			if (currentPair.getDistance() < best) {
				bestPair = currentPair;
			}
		}
		else {
			for (int i = 0; i < Sy.size(); i++) {
				Point p1 = Sy.get(i);
				for (int j = i+1; j < Sy.size() && (j-i+1) <= 8; j++) {
					Point p2 = Sy.get(j);
					Pair currentPair = new Pair(p1, p2);
					if (currentPair.getDistance() < best) {
						best = currentPair.getDistance();
						bestPair = currentPair;
					}
				}
			}
		}
		
		return bestPair;
		
	}
	
	private static Pair closestPair(List<Point> Px, List<Point> Py) {
		//base case
		int numPoints = Px.size();
		if (numPoints <= 3) { //use the brute force method
			return bruteForce(Px);
		}
		else {
			//form Qx, Qx, Rx, Ry from Px and Py
			int k = numPoints/2;
			double medianXValue = Px.get(k-1).getX();
			
			//Create Qx and Rx: O(n)
			List<Point> Qx = new ArrayList<Point>();
			List<Point> Rx = new ArrayList<Point>();
			
			for (int i = 0; i < k; i++) {
				Qx.add(Px.get(i));
			}
			for (int i = k; i < numPoints; i++) {
				Rx.add(Px.get(i));
			}
			
			//Create Qy and Ry O(n)
			List<Point> Qy = new ArrayList<Point>();
			List<Point> Ry = new ArrayList<Point>();
			for (int i = 0; i < numPoints; i++) {
				if (Py.get(i).getX() > medianXValue) {
					Ry.add(Py.get(i));
				}
				else {
					Qy.add(Py.get(i));
				}
			}
			Pair p1 = closestPair(Qx, Qy);
			Pair p2 = closestPair(Rx, Ry);
			double delta = Math.min(p1.getDistance(), p2.getDistance());
			Pair p3 = closestSplitPair(Px, Py, delta);
			return minOfThree(p1, p2, p3);	
		}
	}
	
	public static Pair findClosestPair(List <Point> points) {
		
		int numberPoints = points.size();
		
		//Create Px: O(nlogn) + O(n)
		Collections.sort(points, new PointSortByXCoordinate());
		List<Point> Px = new ArrayList<Point>();
		for (int i = 0; i < numberPoints; i++) {
			Px.add(points.get(i));
		}
		
		//Create Py: O(nlogn) + O(n)
		Collections.sort(points, new PointSortByYCoordinate());
		List<Point> Py = new ArrayList<Point>();
		for (int i = 0; i < numberPoints; i++) {
			Py.add(points.get(i));
		}
		
		return closestPair(Px, Py);
	}
	
	public static Pair bruteForce(List<Point> points) {
		int numPoints = points.size();
		Pair closestPair = new Pair();
		double minimumDistance = Double.MAX_VALUE;
		for (int i = 0; i < numPoints - 1; i++) {
			for (int j = i+1; j < numPoints; j++) {
				Pair pair = new Pair(points.get(i), points.get(j));
				if (pair.getDistance() < minimumDistance) {
					minimumDistance = pair.getDistance();
					closestPair = pair;
				}
			}
		}
		return closestPair;
	}
	public static void main(String[] args) {
		
		 
		List<Point> points = new ArrayList<Point>();
		int numberPoints = 10000;
		//for (int j = 0; j < 100; j++) {
			for (int i = 0; i < numberPoints; i++) {
				double x = Math.random() * 5;
				double y = Math.random() * 5;
				points.add(new Point(x, y));
			}
			
			//calculate brute force method to check later
			long start = System.currentTimeMillis();    
			Pair closestPair = bruteForce(points);
			long elapsedTime = System.currentTimeMillis() - start;
			System.out.println("Brute Force Time: " + elapsedTime + "ms");
			System.out.println("\nClosest Pair via BruteForce Algorithm: ");
			System.out.println(closestPair);
			
			start = System.currentTimeMillis();
			Pair closestPair2 = findClosestPair(points);
			elapsedTime = System.currentTimeMillis() - start;
			System.out.println("\nDivide & Conquer Time: " + elapsedTime + "ms");
			System.out.println("\nClosestPair via Divide&Conquer Algorithm: ");
			System.out.println(closestPair2);
			
			boolean Test =  Math.abs(closestPair.getDistance() - closestPair2.getDistance()) < EPSILON;
			assert Test : "ERROR!!!!!!";
			System.out.println("My test was " + Test + "\n");
		
			//Savings from the geometric proof that you must only check nearest 8 positions
 			//For large n, it becomes substantial
			/*int n = 100; 
			int[] A = new int[n];
			for (int i = 0; i < n;i++) {
				A[i] = i;
			}
			int count = 0;
			for (int i = 0; i < n; i++) {
				int a = i;
				for (int j = i+1; j < n && (j-i+1) <= 8; j++) {
					int b = j;
					System.out.println("(" + a + ", " + b + ")");
					count++;
				}
			}
			System.out.println("Count: " + count);
			System.out.println("n choose 2: " + (n*(n-1))/2);*/
	}
	
		
}
