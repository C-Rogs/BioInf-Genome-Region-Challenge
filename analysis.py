import heapq
import matplotlib.pyplot as plt

#Using a class to enable the analysis to be incorporated into other code easily.
class GenomeRegions:
    def read_regions(self, input_file):
        regions = []
        #The with component helps to manage resources by ensuring the file is closed properly after use. 
        with open(input_file, 'r') as file:
            for line in file:
                #The text file can be read into values using the split function and casting the resulting coordinates into integers.
                start, end = map(int, line.split('\t')) 
                regions.append((start, end))
        return regions

    #This assigns each region to a row so that overlapping regions can be stacked to save space when visualising. 
    def calculate_rows(self, regions):
        #A heap is used to store the end positions of regions to be compared since the regions have already been sorted. It is initialised with the first region.
        heap = [regions[0][1]]
        #To simplify processing, the first region is selected to be on the first row.
        rows = [(0, regions[0][0], regions[0][1])]
        
        for region in regions[1:]:
            while heap and heap[0] <= region[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, region[1])
            rows.append((len(heap) - 1, region[0], region[1])) 
        return rows
    
    #This counts the occourence of overlapping regions which can be used to display a histogram of the genome regions.
    def segmentation(self,regions):
        #Establish a list of points of interest which indicate the start and end points of all the regions so they can be sorted and scanned.
        events = [(start, -1) for start, end in regions]
        #Append the end coordinates of the regions to the end of the event list.
        events += [(end, 0) for start, end in regions]

        #Sorting large sets of data is not ideal, but the inbuilt Python algorithm works faster than a custom method because it is implemented directly in C which is often faster than Python. 
        events.sort()
        counter = 0
        segments = []
        last_coordinate = None
        
        #Event type -1 signifies the start of a region whilst 0 signifies the end of a region and that the count of overlapping regions can be decreased. 
        for end_coordinate, event_type in events:
            # If the counter is not zero and the coordinate has changed add the segment to the results.
            if counter > 0 and last_coordinate is not None and end_coordinate != last_coordinate:
                segments.append((counter, last_coordinate, end_coordinate))
            
            if event_type == -1:  #Starting event
                counter += 1
            elif event_type == 0:  #Ending event
                counter -= 1
            last_coordinate = end_coordinate
        return segments
    
    #Plotting the results to perform a sanity check on the data as it is difficult to verify correctness through only coordinates. 
    #It will only run if the user has Matplotlib installed and is not mandatory. 
    def plot_rows(self, rows, output_file):
        for row in rows:
            plt.plot([row[1], row[2]], [row[0], row[0]], color='blue')

        plt.xlabel('Position on the genome')
        plt.ylabel('Row number')
        plt.title('Genome Regions - Overlapping Graph')
        plt.savefig(output_file)

    def plot_segments(self, segments, output_file):
        for segment in segments:
            plt.plot([segment[1], segment[2]], [segment[0], segment[0]], color='red')

        plt.xlabel('Position on the genome')
        plt.ylabel('Number of overlapping segments')
        plt.title('Genome Segments - Histogram')
        plt.savefig(output_file)


    #This function can write the output for part one and two of the question as they have the same format requirement. 
    def write_output(self, result, output_file):
        with open(output_file, 'w') as file:
            for item in result:
                file.write(f"{item[0]}\t{item[1]}\t{item[2]}\n")

if __name__ == "__main__":
    
    input_files = ["Regions_Small.txt", "Regions_Large.txt"]

    #Instantiate a new GenomeRegion to begin the processing.
    gr = GenomeRegions()

    for input_file in input_files:
        regions = gr.read_regions(input_file)
        #Sort the regions by their starting coordinate 
        regions.sort(key=lambda x: x[0])

        #Part 1
        rows = gr.calculate_rows(regions)
        output_file = f"OutputRows_{input_file}"
        gr.write_output(rows, output_file)

        #Part 2
        segments = gr.segmentation(regions)
        output_file = f"OutputHistogram_{input_file}"
        gr.write_output(segments, output_file)

        #Optional plotting of the graphs for reference. 
        try:
            #Slice the final four characters of the input file name to remove '.txt'. 
            output_file = f"PlotRows_{input_file[:-4]}.png"
            gr.plot_rows(rows,output_file)
            output_file = f"PlotHistogram_{input_file[:-4]}.png"
            gr.plot_segments(segments, output_file)

        except TypeError:
            print("Plotting functions are not available because matplotlib is not installed.")

