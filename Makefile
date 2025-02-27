# Define variables
CSV_DIR := final
CSV_FILES := $(wildcard $(CSV_DIR)/*.csv)
OUTPUT_FILE := $(CSV_DIR)/combined.csv

# Default target: Merge all CSV files
all: merge

merge:
	@echo "🔄 Merging CSV files from '$(CSV_DIR)/' into '$(OUTPUT_FILE)'..."
	@csvstack $(CSV_FILES) > $(OUTPUT_FILE)
	@echo "✅ Merge complete! Output saved as '$(OUTPUT_FILE)'"

clean:
	@echo "🧹 Removing '$(OUTPUT_FILE)'..."
	@rm -f $(OUTPUT_FILE)
	@echo "✅ Cleanup complete!"

help:
	@echo "📌 Available commands:"
	@echo "  make           - Merge all CSV files from '$(CSV_DIR)' into '$(OUTPUT_FILE)'"
	@echo "  make clean     - Remove the merged CSV file"
	@echo "  make help      - Show this help message"
