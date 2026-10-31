import { SearchSelect } from "@/components/shared/SearchSelect";
import React from "react";
import { VISIBLE_ENDPOINT_OPTIONS } from "./chatConstants";

interface EndpointSelectorProps {
  endpointType: string | null;
  onEndpointChange: (value: string | null) => void;
  className?: string;
}

const EndpointSelector: React.FC<EndpointSelectorProps> = ({ endpointType, onEndpointChange, className }) => {
  return (
    <div className={className}>
      <SearchSelect
        value={endpointType}
        onValueChange={onEndpointChange}
        options={VISIBLE_ENDPOINT_OPTIONS}
        placeholder="Select an endpoint"
      />
    </div>
  );
};

export default EndpointSelector;
