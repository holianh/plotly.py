from plotly.basedatatypes import BaseTraceHierarchyType


class Contours(BaseTraceHierarchyType):

    # coloring
    # --------
    @property
    def coloring(self):
        """
        Determines the coloring method showing the contour values. If
        *fill*, coloring is done evenly between each contour level If
        *heatmap*, a heatmap gradient coloring is applied between each
        contour level. If *lines*, coloring is done on the contour
        lines. If *none*, no coloring is applied on this trace.
    
        The 'coloring' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fill', 'heatmap', 'lines', 'none']

        Returns
        -------
        Any
        """
        return self['coloring']

    @coloring.setter
    def coloring(self, val):
        self['coloring'] = val

    # end
    # ---
    @property
    def end(self):
        """
        Sets the end contour level value. Must be more than
        `contours.start`
    
        The 'end' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['end']

    @end.setter
    def end(self, val):
        self['end'] = val

    # labelfont
    # ---------
    @property
    def labelfont(self):
        """
        Sets the font used for labeling the contour levels. The default
        color comes from the lines, if shown. The default family and
        size come from `layout.font`.
    
        The 'labelfont' property is an instance of Labelfont
        that may be specified as:
          - An instance of plotly.graph_objs.histogram2dcontour.contours.Labelfont
          - A dict of string/value properties that will be passed
            to the Labelfont constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.histogram2dcontour.contours.Labelfont
        """
        return self['labelfont']

    @labelfont.setter
    def labelfont(self, val):
        self['labelfont'] = val

    # labelformat
    # -----------
    @property
    def labelformat(self):
        """
        Sets the contour label formatting rule using d3 formatting
        mini-language which is very similar to Python, see: https://git
        hub.com/d3/d3-format/blob/master/README.md#locale_format.
    
        The 'labelformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['labelformat']

    @labelformat.setter
    def labelformat(self, val):
        self['labelformat'] = val

    # operation
    # ---------
    @property
    def operation(self):
        """
        Sets the constraint operation. *=* keeps regions equal to
        `value` *<* and *<=* keep regions less than `value` *>* and
        *>=* keep regions greater than `value` *[]*, *()*, *[)*, and
        *(]* keep regions inside `value[0]` to `value[1]` *][*, *)(*,
        *](*, *)[* keep regions outside `value[0]` to value[1]` Open
        vs. closed intervals make no difference to constraint display,
        but all versions are allowed for consistency with filter
        transforms.
    
        The 'operation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['=', '<', '>=', '>', '<=', '[]', '()', '[)', '(]', '][',
                ')(', '](', ')[']

        Returns
        -------
        Any
        """
        return self['operation']

    @operation.setter
    def operation(self, val):
        self['operation'] = val

    # showlabels
    # ----------
    @property
    def showlabels(self):
        """
        Determines whether to label the contour lines with their
        values.
    
        The 'showlabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlabels']

    @showlabels.setter
    def showlabels(self, val):
        self['showlabels'] = val

    # showlines
    # ---------
    @property
    def showlines(self):
        """
        Determines whether or not the contour lines are drawn. Has an
        effect only if `contours.coloring` is set to *fill*.
    
        The 'showlines' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlines']

    @showlines.setter
    def showlines(self, val):
        self['showlines'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the step between each contour level. Must be positive.
    
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # start
    # -----
    @property
    def start(self):
        """
        Sets the starting contour level value. Must be less than
        `contours.end`
    
        The 'start' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['start']

    @start.setter
    def start(self, val):
        self['start'] = val

    # type
    # ----
    @property
    def type(self):
        """
        If `levels`, the data is represented as a contour plot with
        multiple levels displayed. If `constraint`, the data is
        represented as constraints with the invalid region shaded as
        specified by the `operation` and `value` parameters.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['levels', 'constraint']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the value or values of the constraint boundary. When
        `operation` is set to one of the comparison values
        (=,<,>=,>,<=) *value* is expected to be a number. When
        `operation` is set to one of the interval values
        ([],(),[),(],][,)(,](,)[) *value* is expected to be an array of
        two numbers where the first is the lower bound and the second
        is the upper bound.
    
        The 'value' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'histogram2dcontour'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        coloring
            Determines the coloring method showing the contour
            values. If *fill*, coloring is done evenly between each
            contour level If *heatmap*, a heatmap gradient coloring
            is applied between each contour level. If *lines*,
            coloring is done on the contour lines. If *none*, no
            coloring is applied on this trace.
        end
            Sets the end contour level value. Must be more than
            `contours.start`
        labelfont
            Sets the font used for labeling the contour levels. The
            default color comes from the lines, if shown. The
            default family and size come from `layout.font`.
        labelformat
            Sets the contour label formatting rule using d3
            formatting mini-language which is very similar to
            Python, see: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format.
        operation
            Sets the constraint operation. *=* keeps regions equal
            to `value` *<* and *<=* keep regions less than `value`
            *>* and *>=* keep regions greater than `value` *[]*,
            *()*, *[)*, and *(]* keep regions inside `value[0]` to
            `value[1]` *][*, *)(*, *](*, *)[* keep regions outside
            `value[0]` to value[1]` Open vs. closed intervals make
            no difference to constraint display, but all versions
            are allowed for consistency with filter transforms.
        showlabels
            Determines whether to label the contour lines with
            their values.
        showlines
            Determines whether or not the contour lines are drawn.
            Has an effect only if `contours.coloring` is set to
            *fill*.
        size
            Sets the step between each contour level. Must be
            positive.
        start
            Sets the starting contour level value. Must be less
            than `contours.end`
        type
            If `levels`, the data is represented as a contour plot
            with multiple levels displayed. If `constraint`, the
            data is represented as constraints with the invalid
            region shaded as specified by the `operation` and
            `value` parameters.
        value
            Sets the value or values of the constraint boundary.
            When `operation` is set to one of the comparison values
            (=,<,>=,>,<=) *value* is expected to be a number. When
            `operation` is set to one of the interval values
            ([],(),[),(],][,)(,](,)[) *value* is expected to be an
            array of two numbers where the first is the lower bound
            and the second is the upper bound.
        """

    def __init__(
        self,
        coloring=None,
        end=None,
        labelfont=None,
        labelformat=None,
        operation=None,
        showlabels=None,
        showlines=None,
        size=None,
        start=None,
        type=None,
        value=None,
        **kwargs
    ):
        """
        Construct a new Contours object
        
        Parameters
        ----------
        coloring
            Determines the coloring method showing the contour
            values. If *fill*, coloring is done evenly between each
            contour level If *heatmap*, a heatmap gradient coloring
            is applied between each contour level. If *lines*,
            coloring is done on the contour lines. If *none*, no
            coloring is applied on this trace.
        end
            Sets the end contour level value. Must be more than
            `contours.start`
        labelfont
            Sets the font used for labeling the contour levels. The
            default color comes from the lines, if shown. The
            default family and size come from `layout.font`.
        labelformat
            Sets the contour label formatting rule using d3
            formatting mini-language which is very similar to
            Python, see: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format.
        operation
            Sets the constraint operation. *=* keeps regions equal
            to `value` *<* and *<=* keep regions less than `value`
            *>* and *>=* keep regions greater than `value` *[]*,
            *()*, *[)*, and *(]* keep regions inside `value[0]` to
            `value[1]` *][*, *)(*, *](*, *)[* keep regions outside
            `value[0]` to value[1]` Open vs. closed intervals make
            no difference to constraint display, but all versions
            are allowed for consistency with filter transforms.
        showlabels
            Determines whether to label the contour lines with
            their values.
        showlines
            Determines whether or not the contour lines are drawn.
            Has an effect only if `contours.coloring` is set to
            *fill*.
        size
            Sets the step between each contour level. Must be
            positive.
        start
            Sets the starting contour level value. Must be less
            than `contours.end`
        type
            If `levels`, the data is represented as a contour plot
            with multiple levels displayed. If `constraint`, the
            data is represented as constraints with the invalid
            region shaded as specified by the `operation` and
            `value` parameters.
        value
            Sets the value or values of the constraint boundary.
            When `operation` is set to one of the comparison values
            (=,<,>=,>,<=) *value* is expected to be a number. When
            `operation` is set to one of the interval values
            ([],(),[),(],][,)(,](,)[) *value* is expected to be an
            array of two numbers where the first is the lower bound
            and the second is the upper bound.

        Returns
        -------
        Contours
        """
        super(Contours, self).__init__('contours')

        # Import validators
        # -----------------
        from plotly.validators.histogram2dcontour import (
            contours as v_contours
        )

        # Initialize validators
        # ---------------------
        self._validators['coloring'] = v_contours.ColoringValidator()
        self._validators['end'] = v_contours.EndValidator()
        self._validators['labelfont'] = v_contours.LabelfontValidator()
        self._validators['labelformat'] = v_contours.LabelformatValidator()
        self._validators['operation'] = v_contours.OperationValidator()
        self._validators['showlabels'] = v_contours.ShowlabelsValidator()
        self._validators['showlines'] = v_contours.ShowlinesValidator()
        self._validators['size'] = v_contours.SizeValidator()
        self._validators['start'] = v_contours.StartValidator()
        self._validators['type'] = v_contours.TypeValidator()
        self._validators['value'] = v_contours.ValueValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.coloring = coloring
        self.end = end
        self.labelfont = labelfont
        self.labelformat = labelformat
        self.operation = operation
        self.showlabels = showlabels
        self.showlines = showlines
        self.size = size
        self.start = start
        self.type = type
        self.value = value

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)